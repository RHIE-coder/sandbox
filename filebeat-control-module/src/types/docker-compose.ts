// https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/dockerode-compose/index.d.ts
/**
 * @description "@types/dockerode"에서 DockerodeCompose를 export하지 않아서 types 재선언
 *  */
import * as Dockerode from 'dockerode';

declare namespace DockerodeCompose {
    interface ComposeDownOptions {
        volumes: boolean;
    }

    interface ComposeDownOutput {
        file: string;
        services: [];
        networks: [];
        volumes: [] | undefined;
    }

    interface ComposeUpOptions {
        verbose: boolean;
    }

    interface ComposeUpOutput {
        file: string;
        secrets: any[];
        volumes: Dockerode.VolumeCreateResponse[];
        configs: any[];
        networks: Network[];
        services: Dockerode.Container[];
    }

    interface ComposePullOptions {
        verbose: boolean;
        streams: boolean;
    }

    interface Network {
        name: string;
        network: Dockerode.Network;
    }
}

export = DockerodeCompose;
