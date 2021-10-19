<template>
  <div id="user">
    {{ page_info }}
    <br />
    {{ django_message }}
    <br />
    <table>
      <tr>
        <th>id</th>
        <th>user</th>
      </tr>
      <tr v-for="user in user_list" :key='user'>
        <td>{{ user.pk }}</td>
        <td>{{ user.fields.name }}</td>
      </tr>
    </table>
  </div>
</template>
<script>
export default {
  name: "User",
  data(){
    return {
      page_info: "this User page",
      django_message: "",
      user_list: [],
    }
  },
  created() {
    this.$axios.get("/api/test/")
      .then(response => {
        this.django_message = response.data.message
      });
    this.$axios.get("/api/user/")
      .then(response => {
        this.user_list = JSON.parse(response.data.data)
      })
  }
}
</script>
<style scoped>
</style>

