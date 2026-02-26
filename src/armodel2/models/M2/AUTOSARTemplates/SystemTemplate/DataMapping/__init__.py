"""DataMapping module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
        DataMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_receiver_to_signal_mapping import (
        SenderReceiverToSignalMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_receiver_to_signal_group_mapping import (
        SenderReceiverToSignalGroupMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
        SenderRecCompositeTypeMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_array_type_mapping import (
        SenderRecArrayTypeMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_record_type_mapping import (
        SenderRecRecordTypeMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_record_element_mapping import (
        SenderRecRecordElementMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_array_element_mapping import (
        SenderRecArrayElementMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.indexed_array_element import (
        IndexedArrayElement,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.client_server_to_signal_mapping import (
        ClientServerToSignalMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_receiver_composite_element_to_signal_mapping import (
        SenderReceiverCompositeElementToSignalMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.trigger_to_signal_mapping import (
        TriggerToSignalMapping,
    )

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_type_policy_enum import (
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
