<script setup lang="ts">
defineProps<{
  modelValue?: string,
}>();

defineEmits<{
  (e: 'update:modelValue', value: string): void,
}>();
</script>

<template>
  <input :value="modelValue" @input="$emit('update:modelValue', $event.target?.value)"
         class="w-full mt-1 px-2 py-1 text-black rounded outline-none border-2 focus:border-primary"
         autocomplete="off"/>
</template>
