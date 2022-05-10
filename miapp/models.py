# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
        
    

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    creditos= models.PositiveSmallIntegerField()
    def __unicode__(self):
        return self.nombre


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=1024)
    field_id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='_id_empresa')  # Field renamed because it started with '_'.
    nombre_cliente = models.CharField(max_length=1024)
    telefono_cliente = models.CharField(max_length=50)
    direccion_cliente = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'cliente'


class ClientePedido(models.Model):
    id_pedido = models.OneToOneField('Pedido', models.DO_NOTHING, db_column='id_pedido', primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'cliente_pedido'
        unique_together = (('id_pedido', 'id_cliente'), ('id_pedido', 'id_cliente'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    field_id_empresa = models.CharField(db_column='_id_empresa', primary_key=True, max_length=1024)  # Field renamed because it started with '_'.
    nombre_empresa = models.CharField(max_length=1024)
    telefono_empresa = models.CharField(max_length=30)
    descripcion_empresa = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'
    def __unicode__(self):
        return self.field_id_empresa


class Factura(models.Model):
    id_factura = models.CharField(primary_key=True, max_length=1024)
    field_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='_id_empresa')  # Field renamed because it started with '_'.
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    numero_identificacion_cliente = models.CharField(max_length=1024)
    precio_factura = models.CharField(max_length=200)
    impuestos_factura = models.CharField(max_length=1024)
    fecha_factura = models.DateField()
    si_factura_recurrente = models.BooleanField()
    fecha_factura_recurrente = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'


class Inventario(models.Model):
    id_inventario = models.CharField(primary_key=True, max_length=1024)
    field_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='_id_empresa', blank=True, null=True)  # Field renamed because it started with '_'.
    nombre_inventario = models.CharField(max_length=1024)
    disponibilidad_inventario = models.BooleanField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventario'


class InventarioPedido(models.Model):
    id_pedido = models.OneToOneField('Pedido', models.DO_NOTHING, db_column='id_pedido', primary_key=True)
    id_inventario = models.ForeignKey(Inventario, models.DO_NOTHING, db_column='id_inventario')
    field_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='_id_empresa', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'inventario_pedido'
        unique_together = (('id_pedido', 'id_inventario'), ('id_pedido', 'id_inventario'),)


class Pedido(models.Model):
    id_pedido = models.CharField(primary_key=True, max_length=1024)
    estado_pedido = models.CharField(max_length=1024)
    embalaje_pedido = models.CharField(max_length=1024)
    impuestos_pedido = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoProveedor(models.Model):
    id_proveedor = models.OneToOneField('Proveedor', models.DO_NOTHING, db_column='id_proveedor', primary_key=True)
    id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido')

    class Meta:
        managed = False
        db_table = 'pedido_proveedor'
        unique_together = (('id_proveedor', 'id_pedido'), ('id_proveedor', 'id_pedido'),)


class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=1024)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    nombre_producto = models.CharField(max_length=1024)
    precio_producto = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoInventario(models.Model):
    id_inventario = models.OneToOneField(Inventario, models.DO_NOTHING, db_column='id_inventario', primary_key=True)
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    field_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='_id_empresa', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'producto_inventario'
        unique_together = (('id_inventario', 'id_producto'), ('id_inventario', 'id_producto'),)


class Proveedor(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=1024)
    field_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='_id_empresa')  # Field renamed because it started with '_'.
    nombre_proovedor = models.CharField(max_length=1024)
    nombre_proovedor2 = models.CharField(max_length=1024)
    sede_proovedor = models.CharField(max_length=1024)
    correo_proovedor = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'proveedor'
