"""Transformer module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
        DataTransformation,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_technology import (
        TransformationTechnology,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.buffer_properties import (
        BufferProperties,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
        TransformationDescription,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.end_to_end_transformation_com_spec_props import (
        EndToEndTransformationComSpecProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.e2_e_profile_compatibility_props import (
        E2EProfileCompatibilityProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.end_to_end_transformation_description import (
        EndToEndTransformationDescription,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation_set import (
        DataTransformationSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.user_defined_transformation_description import (
        UserDefinedTransformationDescription,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_i_signal_props import (
        TransformationISignalProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.someip_transformation_description import (
        SOMEIPTransformationDescription,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.someip_transformation_i_signal_props import (
        SOMEIPTransformationISignalProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props_set import (
        TransformationPropsSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
        TransformationProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.someip_transformation_props import (
        SOMEIPTransformationProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_transformation_props import (
        DataPrototypeTransformationProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
        DataPrototypeReference,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_in_port_interface_ref import (
        DataPrototypeInPortInterfaceRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.end_to_end_transformation_i_signal_props import (
        EndToEndTransformationISignalProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.user_defined_transformation_i_signal_props import (
        UserDefinedTransformationISignalProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.user_defined_transformation_props import (
        UserDefinedTransformationProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition_set import (
        TlvDataIdDefinitionSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition import (
        TlvDataIdDefinition,
    )

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation_kind_enum import (
    DataTransformationKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformer_class_enum import (
    TransformerClassEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.cs_transformer_error_reaction_enum import (
    CSTransformerErrorReactionEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.someip_message_type_enum import (
    SOMEIPMessageTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_id_mode_enum import (
    DataIdModeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.end_to_end_profile_behavior_enum import (
    EndToEndProfileBehaviorEnum,
)

__all__ = [
    "BufferProperties",
    "CSTransformerErrorReactionEnum",
    "DataIdModeEnum",
    "DataPrototypeInPortInterfaceRef",
    "DataPrototypeReference",
    "DataPrototypeTransformationProps",
    "DataTransformation",
    "DataTransformationKindEnum",
    "DataTransformationSet",
    "E2EProfileCompatibilityProps",
    "EndToEndProfileBehaviorEnum",
    "EndToEndTransformationComSpecProps",
    "EndToEndTransformationDescription",
    "EndToEndTransformationISignalProps",
    "SOMEIPMessageTypeEnum",
    "SOMEIPTransformationDescription",
    "SOMEIPTransformationISignalProps",
    "SOMEIPTransformationProps",
    "TlvDataIdDefinition",
    "TlvDataIdDefinitionSet",
    "TransformationDescription",
    "TransformationISignalProps",
    "TransformationProps",
    "TransformationPropsSet",
    "TransformationTechnology",
    "TransformerClassEnum",
    "UserDefinedTransformationDescription",
    "UserDefinedTransformationISignalProps",
    "UserDefinedTransformationProps",
]
