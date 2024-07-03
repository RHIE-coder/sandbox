import Docker from 'dockerode';
import Compose from 'dockerode-compose';
import DockerodeCompose from '~/types/docker-compose';

export class DockerError extends Error {
    constructor(message: string) {
        super(message);
    }
}

export class DockerManager {
    private _docker: Docker;
    private static _instance: DockerManager;

    private constructor() {
        this._docker = new Docker({
            socketPath: '/var/run/docker.sock',
        });
    }

    // experiments
    get docker() {
        return this._docker;
    }

    static getInstance(): DockerManager {
        if (!DockerManager._instance) {
            this._instance = new DockerManager();
        }
        return this._instance;
    }

    async getContainerByName(containerName: string): Promise<Docker.ContainerInfo | null> {
        const containers: Array<Docker.ContainerInfo> = await this._docker.listContainers({
            all: true,
            filters: { name: [`/${containerName}`] },
        });

        if (containers.length == 1) {
            return containers[0];
        }
        return null;
    }

    async getContainerById(containerId: string): Promise<Docker.Container> {
        return await this._docker.getContainer(containerId);
    }

    async getNetwork(projectName: string) {
        const networks = await this._docker.listNetworks({
            filters: {
                label: [`com.docker.compose.project=${projectName}`],
            },
        });
        return networks;
    }

    async removeNetwork(projectName: string) {
        const state = await this._docker.pruneNetworks({
            filters: {
                label: [`com.docker.compose.project=${projectName}`],
            },
        });

        return state;
    }

    async composeUp(
        projectName: string,
        composeFilePath: string,
    ): Promise<DockerodeCompose.ComposeUpOutput> {
        const compose = new Compose(this._docker, composeFilePath, projectName);

        try {
            const state = await compose.up({ verbose: true });
            return state;
        } catch (e) {
            await this.removeNetwork(projectName);
            throw new DockerError((e as Error).message);
        }
    }
}
