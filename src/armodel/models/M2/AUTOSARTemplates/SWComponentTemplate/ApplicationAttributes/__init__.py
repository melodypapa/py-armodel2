"""ApplicationAttributes module."""
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_receiver_annotation import (
    SenderReceiverAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_annotation import (
    SenderAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.receiver_annotation import (
    ReceiverAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.client_server_annotation import (
    ClientServerAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.io_hw_abstraction_server_annotation import (
    IoHwAbstractionServerAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.parameter_port_annotation import (
    ParameterPortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.mode_port_annotation import (
    ModePortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.trigger_port_annotation import (
    TriggerPortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.nv_data_port_annotation import (
    NvDataPortAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.delegated_port_annotation import (
    DelegatedPortAnnotation,
)

__all__ = [
    "ClientServerAnnotation",
    "DelegatedPortAnnotation",
    "IoHwAbstractionServerAnnotation",
    "ModePortAnnotation",
    "NvDataPortAnnotation",
    "ParameterPortAnnotation",
    "ReceiverAnnotation",
    "SenderAnnotation",
    "SenderReceiverAnnotation",
    "TriggerPortAnnotation",
]
