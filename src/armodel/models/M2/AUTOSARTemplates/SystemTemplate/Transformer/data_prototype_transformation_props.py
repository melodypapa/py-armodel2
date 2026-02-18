"""DataPrototypeTransformationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 787)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class DataPrototypeTransformationProps(ARObject):
    """AUTOSAR DataPrototypeTransformationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_prototype_in_ref: Optional[ARRef]
    network: Optional[SwDataDefProps]
    transformation_props: Optional[TransformationProps]
    def __init__(self) -> None:
        """Initialize DataPrototypeTransformationProps."""
        super().__init__()
        self.data_prototype_in_ref: Optional[ARRef] = None
        self.network: Optional[SwDataDefProps] = None
        self.transformation_props: Optional[TransformationProps] = None


class DataPrototypeTransformationPropsBuilder:
    """Builder for DataPrototypeTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeTransformationProps = DataPrototypeTransformationProps()

    def build(self) -> DataPrototypeTransformationProps:
        """Build and return DataPrototypeTransformationProps object.

        Returns:
            DataPrototypeTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
