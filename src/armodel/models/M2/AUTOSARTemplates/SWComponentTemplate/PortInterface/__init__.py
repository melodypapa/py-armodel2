"""PortInterface module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
        ArgumentDataPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_interface import (
        ClientServerInterface,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
        ClientServerOperation,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sender_receiver_interface import (
        SenderReceiverInterface,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
        DataInterface,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.nv_data_interface import (
        NvDataInterface,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
        PortInterface,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.parameter_interface import (
        ParameterInterface,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.invalidation_policy import (
        InvalidationPolicy,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.meta_data_item import (
        MetaDataItem,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.meta_data_item_set import (
        MetaDataItemSet,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
        ApplicationError,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.trigger_interface import (
        TriggerInterface,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.mode_switch_interface import (
        ModeSwitchInterface,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping_set import (
        PortInterfaceMappingSet,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
        PortInterfaceMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.variable_and_parameter_interface_mapping import (
        VariableAndParameterInterfaceMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_prototype_mapping import (
        DataPrototypeMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_interface_mapping import (
        ClientServerInterfaceMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation_mapping import (
        ClientServerOperationMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_application_error_mapping import (
        ClientServerApplicationErrorMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.mode_interface_mapping import (
        ModeInterfaceMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.mode_declaration_mapping_set import (
        ModeDeclarationMappingSet,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.mode_declaration_mapping import (
        ModeDeclarationMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.trigger_interface_mapping import (
        TriggerInterfaceMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_mapping import (
        SubElementMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
        SubElementRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.implementation_data_type_sub_element_ref import (
        ImplementationDataTypeSubElementRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_composite_data_type_sub_element_ref import (
        ApplicationCompositeDataTypeSubElementRef,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
        TextTableMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_value_pair import (
        TextTableValuePair,
    )

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.server_argument_impl_policy_enum import (
    ServerArgumentImplPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.mapping_direction_enum import (
    MappingDirectionEnum,
)

__all__ = [
    "ApplicationCompositeDataTypeSubElementRef",
    "ApplicationError",
    "ArgumentDataPrototype",
    "ClientServerApplicationErrorMapping",
    "ClientServerInterface",
    "ClientServerInterfaceMapping",
    "ClientServerOperation",
    "ClientServerOperationMapping",
    "DataInterface",
    "DataPrototypeMapping",
    "ImplementationDataTypeSubElementRef",
    "InvalidationPolicy",
    "MappingDirectionEnum",
    "MetaDataItem",
    "MetaDataItemSet",
    "ModeDeclarationMapping",
    "ModeDeclarationMappingSet",
    "ModeInterfaceMapping",
    "ModeSwitchInterface",
    "NvDataInterface",
    "ParameterInterface",
    "PortInterface",
    "PortInterfaceMapping",
    "PortInterfaceMappingSet",
    "SenderReceiverInterface",
    "ServerArgumentImplPolicyEnum",
    "SubElementMapping",
    "SubElementRef",
    "TextTableMapping",
    "TextTableValuePair",
    "TriggerInterface",
    "TriggerInterfaceMapping",
    "VariableAndParameterInterfaceMapping",
]
