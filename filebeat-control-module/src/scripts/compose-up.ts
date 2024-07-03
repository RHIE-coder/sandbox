import { preloader } from '~/loader/preloader';
import { DockerManager } from '~/manager/docker.manager';

(async () => {
    const config = await preloader();
    const man = DockerManager.getInstance();

    const duplicatedNet = await man.getNetwork(config.projectName);
    if (duplicatedNet.length > 0) {
        const result = await man.removeNetwork(config.projectName);
        console.log(result);
    }

    // console.log(
    //     (await man.docker.listContainers({ all: true })).forEach((container) =>
    //         console.log(container.Names),
    //     ),
    // );
    const alreadyExistContainer = await man.getContainerByName('filebeat');
    if (alreadyExistContainer !== null) {
        const container = await man.getContainerById(alreadyExistContainer.Id);
        await container.remove();
        console.log({ containerDeleted: alreadyExistContainer.Names });
    }

    const state = await man.composeUp(config.projectName, config.buildPath + '/docker-compose.yml');
    console.log(state);
})();
