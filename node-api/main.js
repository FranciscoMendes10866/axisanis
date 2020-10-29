import fastify from 'fastify'

const app = fastify()

app.register(require('fastify-cors'))

app.get('/', (request, reply) => {
    return reply.send({ msg: 'Node API running.' })
})

app.listen(6104, '0.0.0.0')
