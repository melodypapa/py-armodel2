"""ImplementationElementInParameterInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
        ParameterDataPrototype,
    )



class ImplementationElementInParameterInstanceRef(ARObject):
    """AUTOSAR ImplementationElementInParameterInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_ref: Optional[ARRef]
    target_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize ImplementationElementInParameterInstanceRef."""
        super().__init__()
        self.context_ref: Optional[ARRef] = None
        self.target_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ImplementationElementInParameterInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationElementInParameterInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_ref
        if self.context_ref is not None:
            serialized = SerializationHelper.serialize_item(self.context_ref, "ParameterDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_ref
        if self.target_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationElementInParameterInstanceRef":
        """Deserialize XML element to ImplementationElementInParameterInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationElementInParameterInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationElementInParameterInstanceRef, cls).deserialize(element)

        # Parse context_ref
        child = SerializationHelper.find_child_element(element, "CONTEXT-REF")
        if child is not None:
            context_ref_value = ARRef.deserialize(child)
            obj.context_ref = context_ref_value

        # Parse target_ref
        child = SerializationHelper.find_child_element(element, "TARGET-REF")
        if child is not None:
            target_ref_value = ARRef.deserialize(child)
            obj.target_ref = target_ref_value

        return obj



class ImplementationElementInParameterInstanceRefBuilder:
    """Builder for ImplementationElementInParameterInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImplementationElementInParameterInstanceRef = ImplementationElementInParameterInstanceRef()

    def build(self) -> ImplementationElementInParameterInstanceRef:
        """Build and return ImplementationElementInParameterInstanceRef object.

        Returns:
            ImplementationElementInParameterInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
