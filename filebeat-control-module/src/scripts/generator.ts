import * as FS from 'fs/promises';
import * as yaml from 'yaml';
import { preloader } from '~/loader/preloader';
import { DockerManager } from '~/manager/docker.manager';

async function ensureDirectoryExists(directoryPath: string) {
    try {
        await FS.access(directoryPath); // 폴더 접근 시도
    } catch (error) {
        // 폴더가 없는 경우 에러 발생하므로 폴더 생성
        // Error: ENOENT: no such file or director
        if ((error as NodeJS.ErrnoException).code === 'ENOENT') {
            await FS.mkdir(directoryPath, { recursive: true }); // 폴더 생성 (재귀적으로)
        } else {
            throw error; // 다른 종류의 에러인 경우 예외 처리
        }
    }
}

(async () => {
    const config = await preloader();
    const man = DockerManager.getInstance();

    const container = await man.getContainerByName(config.env.CONTAINER_NAME);
    if (container === null) {
        throw new ReferenceError(`${config.env.CONTAINER_NAME} is not exists`);
    }
    const containerId = container.Id;
    const containerName = container.Names[0];

    const compose = await FS.readFile(config.composeFilePath);
    const filebeat = await FS.readFile(config.filebeatFilePath);

    const composeYaml = yaml.parse(Buffer.from(compose).toString());
    const filebeatYaml = yaml.parse(Buffer.from(filebeat).toString());

    composeYaml.services.filebeat.volumes = composeYaml.services.filebeat.volumes.map(
        (volume: string) => {
            return volume
                .replaceAll('${#__PROJECT_PATH__#}', config.projectPath)
                .replaceAll('${#__CONTAINER_ID__#}', containerId);
        },
    );

    composeYaml.services.filebeat.environment.ELASTICSEARCH_HOST = config.env.ELASTICSEARCH_HOST;

    filebeatYaml['filebeat.inputs'] = filebeatYaml['filebeat.inputs'].map((input: any) => {
        if (input.paths) {
            input.paths = input.paths.map((path: string) => {
                return path.replaceAll('${#__CONTAINER_ID__#}', containerId);
            });
        }

        if (input.processors) {
            input.processors.map((processing: any) => {
                if (processing.drop_event) {
                    processing.drop_event.when.or = processing.drop_event.when.or.map(
                        (condition: any) => {
                            if (condition['not.equals.container.name']) {
                                return {
                                    ...condition,
                                    'not.equals.container.name': condition[
                                        'not.equals.container.name'
                                    ].replaceAll(
                                        '${#__CONTAINER_NAME__#}',
                                        containerName.substring(1),
                                    ),
                                };
                            }

                            return condition;
                        },
                    );
                }
            });
        }

        return input;
    });

    console.log(filebeatYaml['filebeat.inputs'][0].processors[1].drop_event.when.or);

    const parsedCompose = yaml.stringify(composeYaml);
    const parsedFilebeat = yaml.stringify(filebeatYaml);

    console.log(parsedFilebeat);
    await ensureDirectoryExists(config.buildPath);

    await Promise.all([
        FS.writeFile(config.buildPath + '/docker-compose.yml', parsedCompose),
        FS.writeFile(config.buildPath + '/filebeat.docker.yml', parsedFilebeat),
    ]);
})();
