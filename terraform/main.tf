resource "docker_image" "pipeline" {
  name         = var.image_name
  keep_locally = true
  build {
    context = ".."
  }
}

resource "docker_container" "pipeline" {
  image = docker_image.pipeline.image_id
  name  = var.container_name
}
