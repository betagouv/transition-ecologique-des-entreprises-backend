import { EtablissementRepository } from './spi.js'

/**
 * Injects infrastructure dependency into domain features
 */
export const createFeatures = (etablissementRepository: EtablissementRepository) => {
  /**
   * fetchEtablissement passes through the Promise of the spi
   * (promise of Etablissement in case of success, Error otherwise)
   */
  const fetchEtablissement = async (siret: string) => {
    return etablissementRepository.getEtablissementBySiret(siret)
  }
  return { fetchEtablissement }
}
