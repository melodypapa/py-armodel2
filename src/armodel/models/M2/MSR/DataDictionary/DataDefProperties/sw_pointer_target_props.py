"""SwPointerTargetProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 39)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 286)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 471)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
        BswModuleEntry,
    )
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



class SwPointerTargetProps(ARObject):
    """AUTOSAR SwPointerTargetProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    function_pointer_ref: Optional[ARRef]
    sw_data_def: Optional[SwDataDefProps]
    target_category: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize SwPointerTargetProps."""
        super().__init__()
        self.function_pointer_ref: Optional[ARRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.target_category: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize SwPointerTargetProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize function_pointer_ref
        if self.function_pointer_ref is not None:
            serialized = SerializationHelper.serialize_item(self.function_pointer_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION-POINTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_data_def
        if self.sw_data_def is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_def, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_category
        if self.target_category is not None:
            serialized = SerializationHelper.serialize_item(self.target_category, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwPointerTargetProps":
        """Deserialize XML element to SwPointerTargetProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwPointerTargetProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse function_pointer_ref
        child = SerializationHelper.find_child_element(element, "FUNCTION-POINTER-REF")
        if child is not None:
            function_pointer_ref_value = ARRef.deserialize(child)
            obj.function_pointer_ref = function_pointer_ref_value

        # Parse sw_data_def
        child = SerializationHelper.find_child_element(element, "SW-DATA-DEF")
        if child is not None:
            sw_data_def_value = SerializationHelper.deserialize_by_tag(child, "SwDataDefProps")
            obj.sw_data_def = sw_data_def_value

        # Parse target_category
        child = SerializationHelper.find_child_element(element, "TARGET-CATEGORY")
        if child is not None:
            target_category_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.target_category = target_category_value

        return obj



class SwPointerTargetPropsBuilder:
    """Builder for SwPointerTargetProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwPointerTargetProps = SwPointerTargetProps()

    def build(self) -> SwPointerTargetProps:
        """Build and return SwPointerTargetProps object.

        Returns:
            SwPointerTargetProps instance
        """
        # TODO: Add validation
        return self._obj
