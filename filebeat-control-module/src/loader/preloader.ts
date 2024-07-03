import * as Dotenv from 'dotenv';
import * as Path from 'path';
import { DockerManager } from '~/manager/docker.manager';

function loadEnvWithValidate(...envKeyCheckList: string[]): Record<string, string> {
    Dotenv.config();

    const env: Record<string, string> = {};

    for (const key of envKeyCheckList) {
        if (process.env[key] === undefined) {
            throw new ReferenceError(`"${key}" is not exists`);
        }
        env[key] = process.env[key];
    }

    return env;
}

function getProjectInfo() {
    const rootPath = Path.join(__dirname, '..', '..');
    return {
        rootPath: rootPath,
        projectName: Path.basename(rootPath),
    };
}

export async function preloader() {
    const env = loadEnvWithValidate('ELASTICSEARCH_HOST', 'NETWORK_NAME', 'CONTAINER_NAME');
    const { rootPath, projectName } = getProjectInfo();
    const composeFilePath = Path.join(rootPath, 'template', 'docker-compose.yml');
    const filebeatFilePath = Path.join(rootPath, 'template', 'filebeat.docker.yml');
    const buildPath = Path.join(rootPath, '.build');
    DockerManager.getInstance();

    return {
        env,
        composeFilePath,
        filebeatFilePath,
        buildPath,
        projectName,
        projectPath: rootPath,
    };
}
