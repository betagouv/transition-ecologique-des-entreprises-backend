import { Request, Response } from 'express'

export const helloWorldRoute = (_: Request, res: Response): void => {
  res.send('Hello world this is multi !!!')
}
