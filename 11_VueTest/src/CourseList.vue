<template>
  <div class="courseslist">
    <div class="course" v-for="course in courses">
      <div class="images">
        <img :src="`../src/assets/img/${course.img}`" alt="" />
      </div>
      <div class="text">
        <router-link :to="`/courses/${course.id}`">
          {{ course.name }}
        </router-link>
        <p>
          Lorem, ipsum dolor sit amet consectetur adipisicing elit. Natus
          doloremque in aperiam amet libero eveniet alias illum! Exercitationem,
          quisquam cum laudantium mollitia molestias voluptatibus praesentium
          itaque esse eligendi voluptate corrupti? Qui at exercitationem
          temporibus nisi. Reiciendis dolore, Odio, fuga. Cupiditate officiis
          consequuntur error ipsa labore?
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      courses: [
        { id: 1, img: "A.jpg", name: "Basic Course" },
        { id: 2, img: "B.jpg", name: "Advance Course" },
        { id: 3, img: "C.jpg", name: "Extreme Course" }
      ]
    };
  }
};
</script>

<style scoped>
.course {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
.text {
  width: 30%;
  margin: 10px 10px;
}

img {
  padding-right: 15px;
  padding-bottom: 30px;
}

a {
  display: inline-block;
  color: #42b983;
  font-size: 1.5em;
  text-decoration: none;
}
</style>
