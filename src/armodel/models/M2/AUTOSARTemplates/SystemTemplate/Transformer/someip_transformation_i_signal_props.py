"""SOMEIPTransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 778)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    SOMEIPMessageTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.tlv_data_id_definition_set import (
    TlvDataIdDefinitionSet,
)


class SOMEIPTransformationISignalProps(ARObject):
    """AUTOSAR SOMEIPTransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    implements: Optional[Boolean]
    interface_version: Optional[PositiveInteger]
    is_dynamic: Optional[Boolean]
    message_type: Optional[SOMEIPMessageTypeEnum]
    size_of_array: Optional[PositiveInteger]
    size_of_string: Optional[PositiveInteger]
    size_of_struct: Optional[PositiveInteger]
    size_of_union: Optional[PositiveInteger]
    tlv_data_id_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize SOMEIPTransformationISignalProps."""
        super().__init__()
        self.implements: Optional[Boolean] = None
        self.interface_version: Optional[PositiveInteger] = None
        self.is_dynamic: Optional[Boolean] = None
        self.message_type: Optional[SOMEIPMessageTypeEnum] = None
        self.size_of_array: Optional[PositiveInteger] = None
        self.size_of_string: Optional[PositiveInteger] = None
        self.size_of_struct: Optional[PositiveInteger] = None
        self.size_of_union: Optional[PositiveInteger] = None
        self.tlv_data_id_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationISignalProps":
        """Deserialize XML element to SOMEIPTransformationISignalProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SOMEIPTransformationISignalProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse implements
        child = ARObject._find_child_element(element, "IMPLEMENTS")
        if child is not None:
            implements_value = child.text
            obj.implements = implements_value

        # Parse interface_version
        child = ARObject._find_child_element(element, "INTERFACE-VERSION")
        if child is not None:
            interface_version_value = child.text
            obj.interface_version = interface_version_value

        # Parse is_dynamic
        child = ARObject._find_child_element(element, "IS-DYNAMIC")
        if child is not None:
            is_dynamic_value = child.text
            obj.is_dynamic = is_dynamic_value

        # Parse message_type
        child = ARObject._find_child_element(element, "MESSAGE-TYPE")
        if child is not None:
            message_type_value = child.text
            obj.message_type = message_type_value

        # Parse size_of_array
        child = ARObject._find_child_element(element, "SIZE-OF-ARRAY")
        if child is not None:
            size_of_array_value = child.text
            obj.size_of_array = size_of_array_value

        # Parse size_of_string
        child = ARObject._find_child_element(element, "SIZE-OF-STRING")
        if child is not None:
            size_of_string_value = child.text
            obj.size_of_string = size_of_string_value

        # Parse size_of_struct
        child = ARObject._find_child_element(element, "SIZE-OF-STRUCT")
        if child is not None:
            size_of_struct_value = child.text
            obj.size_of_struct = size_of_struct_value

        # Parse size_of_union
        child = ARObject._find_child_element(element, "SIZE-OF-UNION")
        if child is not None:
            size_of_union_value = child.text
            obj.size_of_union = size_of_union_value

        # Parse tlv_data_id_refs (list)
        obj.tlv_data_id_refs = []
        for child in ARObject._find_all_child_elements(element, "TLV-DATA-IDS"):
            tlv_data_id_refs_value = ARObject._deserialize_by_tag(child, "TlvDataIdDefinitionSet")
            obj.tlv_data_id_refs.append(tlv_data_id_refs_value)

        return obj



class SOMEIPTransformationISignalPropsBuilder:
    """Builder for SOMEIPTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationISignalProps = SOMEIPTransformationISignalProps()

    def build(self) -> SOMEIPTransformationISignalProps:
        """Build and return SOMEIPTransformationISignalProps object.

        Returns:
            SOMEIPTransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
