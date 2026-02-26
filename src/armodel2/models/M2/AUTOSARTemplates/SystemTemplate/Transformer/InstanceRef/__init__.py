"""InstanceRef module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef.data_prototype_in_sender_receiver_interface_instance_ref import (
        DataPrototypeInSenderReceiverInterfaceInstanceRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef.data_prototype_in_client_server_interface_instance_ref import (
        DataPrototypeInClientServerInterfaceInstanceRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef.implementation_data_type_element_in_port_interface_ref import (
        ImplementationDataTypeElementInPortInterfaceRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef.data_prototype_in_port_interface_instance_ref import (
        DataPrototypeInPortInterfaceInstanceRef,
    )

__all__ = [
    "DataPrototypeInClientServerInterfaceInstanceRef",
    "DataPrototypeInPortInterfaceInstanceRef",
    "DataPrototypeInSenderReceiverInterfaceInstanceRef",
    "ImplementationDataTypeElementInPortInterfaceRef",
]
