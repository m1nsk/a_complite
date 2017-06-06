import axios from 'axios'
import { API_HOST, API_PORT } from '../api/config'

export const baseHost = `${API_HOST}:${API_PORT}`
export const baseURL = baseHost + '/api/'

axios.defaults.baseURL = baseURL

export function getBookByAuthor (query) {
  return axios.get('/complete/author/' + query)
}

export function getBookByPublisher (query) {
  return axios.get('/complete/publisher/' + query)
}

export function addBookFromForm (formData) {
  const config = {
    headers: {
      'content-type': 'multipart/form-data',
      'Content-Type': 'application/json'
    }
  }
  return axios.post('/book/add/', formData, config)
}
