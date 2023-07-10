import type { Config } from '@jest/types'

// Sync object
const config: Config.InitialOptions = {
  verbose: true,
  testEnvironment: 'node',
  // moduleDirectories: [
  //   "<rootDir>/node_modules",
  //   // "../../node_modules",
  //   // "node_modules"
  // ],
  // transformIgnorePatterns: [
  //   // "node_modules/(?!variables/.*)",
  //   "node_modules"
  // ],
  transform: {
    '^.+\\.(ts|tsx)?$': 'ts-jest'
  },
  // preset: 'ts-jest'
}
export default config
