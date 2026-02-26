"""Datatypes module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
        ApplicationDataType,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
        AutosarDataType,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
        DataTypeMappingSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_primitive_data_type import (
        ApplicationPrimitiveDataType,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_map import (
        DataTypeMap,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import (
        ApplicationCompositeDataType,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_array_data_type import (
        ApplicationArrayDataType,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_record_data_type import (
        ApplicationRecordDataType,
    )

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.array_size_handling_enum import (
    ArraySizeHandlingEnum,
)

__all__ = [
    "ApplicationArrayDataType",
    "ApplicationCompositeDataType",
    "ApplicationDataType",
    "ApplicationPrimitiveDataType",
    "ApplicationRecordDataType",
    "ArraySizeHandlingEnum",
    "AutosarDataType",
    "DataTypeMap",
    "DataTypeMappingSet",
]
