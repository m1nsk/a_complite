import axios from 'axios'
import { API_HOST, API_PORT } from '../api/config'

export const baseHost = `${API_HOST}:${API_PORT}`
export const baseURL = baseHost + '/api/'

axios.defaults.baseURL = baseURL

export function getBookByField (data) {
  return axios.get('/complete/', {
    params: data
  })
}

export function postBook (formData) {
  const config = {
    headers: {
      'content-type': 'multipart/form-data',
      'content-Type': 'application/json'
    }
  }
  return axios.post('/book/', formData, config)
}

export function postAuthor (formData) {
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }
  return axios.post('/author/', formData, config)
}

export function postPublisher (formData) {
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }
  return axios.post('/publisher/', formData, config)
}

export function getAuthorList () {
  return axios.get('/author/')
}

export function getPublisherList () {
  return axios.get('/publisher/')
}

export function getAuthorById (id) {
  return axios.get('/author/' + id)
}

export function getPublisherById (id) {
  return axios.get('/publisher/' + id)
}

export function deleteAuthorById (id) {
  return axios.delete('/author/' + id)
}

export function deletePublisherById (id) {
  return axios.delete('/publisher/' + id)
}

export function putAuthor (id, formData) {
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }
  return axios.put('/author/' + id + '/', formData, config)
}

export function putPublisher (id, formData) {
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }
  return axios.put('/publisher/' + id + '/', formData, config)
}
