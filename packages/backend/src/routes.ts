import { Request, Response } from 'express'
import app from './index'

app.get('/', (_: Request, res: Response): void => {
  res.send('Hello world')
})
