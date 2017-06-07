import axios from 'axios'
import { API_HOST, API_PORT } from '../api/config'

export const baseHost = `${API_HOST}:${API_PORT}`
export const baseURL = baseHost + '/api/'

axios.defaults.baseURL = baseURL

export function getBookByField (data) {
  console.log(data)
  return axios.get('/complete/', {
    params: data
  })
}

export function getBookByPublisher (query) {
  return axios.get('/complete/publisher/' + query)
}

export function addBookFrom (formData) {
  const config = {
    headers: {
      'content-type': 'multipart/form-data',
      'Content-Type': 'application/json'
    }
  }
  return axios.post('/book/', formData, config)
}

export function addAuthorFrom (formData) {
  const config = {
    headers: {
      'content-type': 'multipart/form-data',
      'Content-Type': 'application/json'
    }
  }
  return axios.post('/author/', formData, config)
}

export function addPublisherFrom (formData) {
  const config = {
    headers: {
      'content-type': 'multipart/form-data',
      'Content-Type': 'application/json'
    }
  }
  return axios.post('/publisher/', formData, config)
}
