"""PortPrototypeBlueprintInitValue AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 60)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintDedicated_Port.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class PortPrototypeBlueprintInitValue(ARObject):
    """AUTOSAR PortPrototypeBlueprintInitValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_prototype_ref: ARRef
    value: ValueSpecification
    def __init__(self) -> None:
        """Initialize PortPrototypeBlueprintInitValue."""
        super().__init__()
        self.data_prototype_ref: ARRef = None
        self.value: ValueSpecification = None

    def serialize(self) -> ET.Element:
        """Serialize PortPrototypeBlueprintInitValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortPrototypeBlueprintInitValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_prototype_ref
        if self.data_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_prototype_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortPrototypeBlueprintInitValue":
        """Deserialize XML element to PortPrototypeBlueprintInitValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortPrototypeBlueprintInitValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortPrototypeBlueprintInitValue, cls).deserialize(element)

        # Parse data_prototype_ref
        child = SerializationHelper.find_child_element(element, "DATA-PROTOTYPE-REF")
        if child is not None:
            data_prototype_ref_value = ARRef.deserialize(child)
            obj.data_prototype_ref = data_prototype_ref_value

        # Parse value
        child = SerializationHelper.find_child_element(element, "VALUE")
        if child is not None:
            value_value = SerializationHelper.deserialize_by_tag(child, "ValueSpecification")
            obj.value = value_value

        return obj



class PortPrototypeBlueprintInitValueBuilder:
    """Builder for PortPrototypeBlueprintInitValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortPrototypeBlueprintInitValue = PortPrototypeBlueprintInitValue()

    def build(self) -> PortPrototypeBlueprintInitValue:
        """Build and return PortPrototypeBlueprintInitValue object.

        Returns:
            PortPrototypeBlueprintInitValue instance
        """
        # TODO: Add validation
        return self._obj
