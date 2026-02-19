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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeTransformationProps":
        """Deserialize XML element to DataPrototypeTransformationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeTransformationProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_prototype_in_ref
        child = ARObject._find_child_element(element, "DATA-PROTOTYPE-IN")
        if child is not None:
            data_prototype_in_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.data_prototype_in_ref = data_prototype_in_ref_value

        # Parse network
        child = ARObject._find_child_element(element, "NETWORK")
        if child is not None:
            network_value = ARObject._deserialize_by_tag(child, "SwDataDefProps")
            obj.network = network_value

        # Parse transformation_props
        child = ARObject._find_child_element(element, "TRANSFORMATION-PROPS")
        if child is not None:
            transformation_props_value = ARObject._deserialize_by_tag(child, "TransformationProps")
            obj.transformation_props = transformation_props_value

        return obj



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
