from django.db import models

class Services(models.Model):
    client_name = models.CharField("Nome do cliente", max_length=255, null=False, blank=False)
    client_contact = models.CharField("Contatodo cliente", max_length=255, null=False, blank=False)
    head_model = models.CharField("Modelo do cabeçote", max_length=255, null=False, blank=False)
    start_date = models.DateField("Data de ínicio", null=False, blank=False)
    order_of_service = models.CharField("Ordem de serviço", primary_key=True, max_length=255, null=False, blank=False)
    guarantee = models.IntegerField("Tempo de garantia", default=0)
    grind = models.BooleanField("Esmerilhar", default=False)
    weld = models.BooleanField("Soldar", default=False)
    pleinar = models.BooleanField("Pleinar", default=False)
    to_wash = models.BooleanField("Lavar", default=False)
    washclean_valves = models.BooleanField("Limpar válvulas", default=False)
    to_polish = models.BooleanField("Polir", default=False)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self) -> str:
        return "OS{} - {} - Feito em {}".format(self.order_of_service, self.head_model, self.start_date)