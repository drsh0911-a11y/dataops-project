output "container_name" {
  value = docker_container.pipeline.name
}

output "container_id" {
  value = docker_container.pipeline.id
}

output "image_name" {
  value = docker_image.pipeline.name
}
