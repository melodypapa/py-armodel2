"""McSwEmulationMethodSupport AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_parameter_element_group import (
    McParameterElementGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class McSwEmulationMethodSupport(ARObject):
    """AUTOSAR McSwEmulationMethodSupport."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_reference_ref: Optional[ARRef]
    category: Optional[Identifier]
    element_groups: list[McParameterElementGroup]
    reference_table_ref: Optional[ARRef]
    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize McSwEmulationMethodSupport."""
        super().__init__()
        self.base_reference_ref: Optional[ARRef] = None
        self.category: Optional[Identifier] = None
        self.element_groups: list[McParameterElementGroup] = []
        self.reference_table_ref: Optional[ARRef] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize McSwEmulationMethodSupport to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize base_reference_ref
        if self.base_reference_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_reference_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REFERENCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_groups (list to container "ELEMENT-GROUPS")
        if self.element_groups:
            wrapper = ET.Element("ELEMENT-GROUPS")
            for item in self.element_groups:
                serialized = SerializationHelper.serialize_item(item, "McParameterElementGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reference_table_ref
        if self.reference_table_ref is not None:
            serialized = SerializationHelper.serialize_item(self.reference_table_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERENCE-TABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McSwEmulationMethodSupport":
        """Deserialize XML element to McSwEmulationMethodSupport object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McSwEmulationMethodSupport object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base_reference_ref
        child = SerializationHelper.find_child_element(element, "BASE-REFERENCE-REF")
        if child is not None:
            base_reference_ref_value = ARRef.deserialize(child)
            obj.base_reference_ref = base_reference_ref_value

        # Parse category
        child = SerializationHelper.find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.category = category_value

        # Parse element_groups (list from container "ELEMENT-GROUPS")
        obj.element_groups = []
        container = SerializationHelper.find_child_element(element, "ELEMENT-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.element_groups.append(child_value)

        # Parse reference_table_ref
        child = SerializationHelper.find_child_element(element, "REFERENCE-TABLE-REF")
        if child is not None:
            reference_table_ref_value = ARRef.deserialize(child)
            obj.reference_table_ref = reference_table_ref_value

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        return obj



class McSwEmulationMethodSupportBuilder:
    """Builder for McSwEmulationMethodSupport."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McSwEmulationMethodSupport = McSwEmulationMethodSupport()

    def build(self) -> McSwEmulationMethodSupport:
        """Build and return McSwEmulationMethodSupport object.

        Returns:
            McSwEmulationMethodSupport instance
        """
        # TODO: Add validation
        return self._obj
