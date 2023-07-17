import { Etablissement } from './types.js'

export type fetchEtablissement = (siret: string) => Promise<Etablissement>
