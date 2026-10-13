"""Cria tabelas de produtos, estoques e entregas."""
from alembic import op
import sqlalchemy as sa

revision = "0001_logistica"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table("produtos", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("nome", sa.String(120), nullable=False), sa.Column("sku", sa.String(40), nullable=False), sa.Column("unidade", sa.String(20), nullable=False))
    op.create_index("ix_produtos_id", "produtos", ["id"])
    op.create_index("ix_produtos_sku", "produtos", ["sku"], unique=True)
    op.create_table("estoques", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("produto_id", sa.Integer(), sa.ForeignKey("produtos.id", ondelete="RESTRICT"), nullable=False), sa.Column("local", sa.String(120), nullable=False), sa.Column("quantidade", sa.Integer(), nullable=False), sa.Column("reservada", sa.Integer(), nullable=False, server_default="0"), sa.CheckConstraint("quantidade >= 0", name="ck_estoque_quantidade_nao_negativa"), sa.CheckConstraint("reservada >= 0 AND reservada <= quantidade", name="ck_estoque_reservada_valida"), sa.UniqueConstraint("produto_id", "local", name="uq_estoque_produto_local"))
    op.create_index("ix_estoques_id", "estoques", ["id"])
    op.create_index("ix_estoques_produto_id", "estoques", ["produto_id"])
    op.create_table("entregas", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("codigo_rastreamento", sa.String(50), nullable=False), sa.Column("destinatario", sa.String(120), nullable=False), sa.Column("estoque_id", sa.Integer(), sa.ForeignKey("estoques.id", ondelete="RESTRICT"), nullable=False), sa.Column("quantidade", sa.Integer(), nullable=False), sa.Column("endereco_entrega", sa.String(240), nullable=False), sa.Column("status", sa.String(20), nullable=False, server_default="CRIADA"), sa.Column("criada_em", sa.DateTime(timezone=True), nullable=False))
    op.create_index("ix_entregas_id", "entregas", ["id"])
    op.create_index("ix_entregas_estoque_id", "entregas", ["estoque_id"])
    op.create_index("ix_entregas_codigo_rastreamento", "entregas", ["codigo_rastreamento"], unique=True)

def downgrade():
    op.drop_table("entregas")
    op.drop_table("estoques")
    op.drop_table("produtos")
