"""DataPrototypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 125)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2014)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_mapping import (
    SubElementMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class DataPrototypeMapping(ARObject):
    """AUTOSAR DataPrototypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_data_ref: Optional[ARRef]
    first_to_second: Optional[DataTransformation]
    second_data_ref: Optional[ARRef]
    second_to_first: Optional[DataTransformation]
    sub_element_refs: list[ARRef]
    text_table_ref: ARRef
    def __init__(self) -> None:
        """Initialize DataPrototypeMapping."""
        super().__init__()
        self.first_data_ref: Optional[ARRef] = None
        self.first_to_second: Optional[DataTransformation] = None
        self.second_data_ref: Optional[ARRef] = None
        self.second_to_first: Optional[DataTransformation] = None
        self.sub_element_refs: list[ARRef] = []
        self.text_table_ref: ARRef = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeMapping":
        """Deserialize XML element to DataPrototypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse first_data_ref
        child = ARObject._find_child_element(element, "FIRST-DATA")
        if child is not None:
            first_data_ref_value = ARObject._deserialize_by_tag(child, "AutosarDataPrototype")
            obj.first_data_ref = first_data_ref_value

        # Parse first_to_second
        child = ARObject._find_child_element(element, "FIRST-TO-SECOND")
        if child is not None:
            first_to_second_value = ARObject._deserialize_by_tag(child, "DataTransformation")
            obj.first_to_second = first_to_second_value

        # Parse second_data_ref
        child = ARObject._find_child_element(element, "SECOND-DATA")
        if child is not None:
            second_data_ref_value = ARObject._deserialize_by_tag(child, "AutosarDataPrototype")
            obj.second_data_ref = second_data_ref_value

        # Parse second_to_first
        child = ARObject._find_child_element(element, "SECOND-TO-FIRST")
        if child is not None:
            second_to_first_value = ARObject._deserialize_by_tag(child, "DataTransformation")
            obj.second_to_first = second_to_first_value

        # Parse sub_element_refs (list)
        obj.sub_element_refs = []
        for child in ARObject._find_all_child_elements(element, "SUB-ELEMENTS"):
            sub_element_refs_value = ARObject._deserialize_by_tag(child, "SubElementMapping")
            obj.sub_element_refs.append(sub_element_refs_value)

        # Parse text_table_ref
        child = ARObject._find_child_element(element, "TEXT-TABLE")
        if child is not None:
            text_table_ref_value = ARObject._deserialize_by_tag(child, "TextTableMapping")
            obj.text_table_ref = text_table_ref_value

        return obj



class DataPrototypeMappingBuilder:
    """Builder for DataPrototypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeMapping = DataPrototypeMapping()

    def build(self) -> DataPrototypeMapping:
        """Build and return DataPrototypeMapping object.

        Returns:
            DataPrototypeMapping instance
        """
        # TODO: Add validation
        return self._obj
