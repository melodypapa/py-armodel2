"""DataMapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
        DataMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_receiver_to_signal_mapping import (
        SenderReceiverToSignalMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_receiver_to_signal_group_mapping import (
        SenderReceiverToSignalGroupMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
        SenderRecCompositeTypeMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_array_type_mapping import (
        SenderRecArrayTypeMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_record_type_mapping import (
        SenderRecRecordTypeMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_record_element_mapping import (
        SenderRecRecordElementMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_array_element_mapping import (
        SenderRecArrayElementMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.indexed_array_element import (
        IndexedArrayElement,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.client_server_to_signal_mapping import (
        ClientServerToSignalMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_receiver_composite_element_to_signal_mapping import (
        SenderReceiverCompositeElementToSignalMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.trigger_to_signal_mapping import (
        TriggerToSignalMapping,
    )

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_type_policy_enum import (
    DataTypePolicyEnum,
)

__all__ = [
    "ClientServerToSignalMapping",
    "DataMapping",
    "DataTypePolicyEnum",
    "IndexedArrayElement",
    "SenderRecArrayElementMapping",
    "SenderRecArrayTypeMapping",
    "SenderRecCompositeTypeMapping",
    "SenderRecRecordElementMapping",
    "SenderRecRecordTypeMapping",
    "SenderReceiverCompositeElementToSignalMapping",
    "SenderReceiverToSignalGroupMapping",
    "SenderReceiverToSignalMapping",
    "TriggerToSignalMapping",
]
