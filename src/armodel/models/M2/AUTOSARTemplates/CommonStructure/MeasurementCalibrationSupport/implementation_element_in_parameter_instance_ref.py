"""ImplementationElementInParameterInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    target: Optional[Any]
    def __init__(self) -> None:
        """Initialize ImplementationElementInParameterInstanceRef."""
        super().__init__()
        self.context_ref: Optional[ARRef] = None
        self.target: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ImplementationElementInParameterInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize context_ref
        if self.context_ref is not None:
            serialized = ARObject._serialize_item(self.context_ref, "ParameterDataPrototype")
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

        # Serialize target
        if self.target is not None:
            serialized = ARObject._serialize_item(self.target, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_ref
        child = ARObject._find_child_element(element, "CONTEXT-REF")
        if child is not None:
            context_ref_value = ARRef.deserialize(child)
            obj.context_ref = context_ref_value

        # Parse target
        child = ARObject._find_child_element(element, "TARGET")
        if child is not None:
            target_value = child.text
            obj.target = target_value

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
