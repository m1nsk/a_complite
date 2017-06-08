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
      'content-type': 'multipart/form-data',
      'Content-Type': 'application/json'
    }
  }
  return axios.post('/author/', formData, config)
}

export function postPublisher (formData) {
  const config = {
    headers: {
      'content-type': 'multipart/form-data',
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
