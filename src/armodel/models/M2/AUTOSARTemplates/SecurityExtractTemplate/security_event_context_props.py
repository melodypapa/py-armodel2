"""SecurityEventContextProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 258)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 33)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_definition import (
    SecurityEventDefinition,
)


class SecurityEventContextProps(Identifiable):
    """AUTOSAR SecurityEventContextProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_data: Optional[Any]
    default: Optional[Any]
    persistent: Optional[Boolean]
    security_event: Optional[SecurityEventDefinition]
    sensor_instance: Optional[PositiveInteger]
    severity: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecurityEventContextProps."""
        super().__init__()
        self.context_data: Optional[Any] = None
        self.default: Optional[Any] = None
        self.persistent: Optional[Boolean] = None
        self.security_event: Optional[SecurityEventDefinition] = None
        self.sensor_instance: Optional[PositiveInteger] = None
        self.severity: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize SecurityEventContextProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventContextProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_data
        if self.context_data is not None:
            serialized = ARObject._serialize_item(self.context_data, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default
        if self.default is not None:
            serialized = ARObject._serialize_item(self.default, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize persistent
        if self.persistent is not None:
            serialized = ARObject._serialize_item(self.persistent, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERSISTENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_event
        if self.security_event is not None:
            serialized = ARObject._serialize_item(self.security_event, "SecurityEventDefinition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURITY-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sensor_instance
        if self.sensor_instance is not None:
            serialized = ARObject._serialize_item(self.sensor_instance, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SENSOR-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize severity
        if self.severity is not None:
            serialized = ARObject._serialize_item(self.severity, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEVERITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextProps":
        """Deserialize XML element to SecurityEventContextProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventContextProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventContextProps, cls).deserialize(element)

        # Parse context_data
        child = ARObject._find_child_element(element, "CONTEXT-DATA")
        if child is not None:
            context_data_value = child.text
            obj.context_data = context_data_value

        # Parse default
        child = ARObject._find_child_element(element, "DEFAULT")
        if child is not None:
            default_value = child.text
            obj.default = default_value

        # Parse persistent
        child = ARObject._find_child_element(element, "PERSISTENT")
        if child is not None:
            persistent_value = child.text
            obj.persistent = persistent_value

        # Parse security_event
        child = ARObject._find_child_element(element, "SECURITY-EVENT")
        if child is not None:
            security_event_value = ARObject._deserialize_by_tag(child, "SecurityEventDefinition")
            obj.security_event = security_event_value

        # Parse sensor_instance
        child = ARObject._find_child_element(element, "SENSOR-INSTANCE")
        if child is not None:
            sensor_instance_value = child.text
            obj.sensor_instance = sensor_instance_value

        # Parse severity
        child = ARObject._find_child_element(element, "SEVERITY")
        if child is not None:
            severity_value = child.text
            obj.severity = severity_value

        return obj



class SecurityEventContextPropsBuilder:
    """Builder for SecurityEventContextProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextProps = SecurityEventContextProps()

    def build(self) -> SecurityEventContextProps:
        """Build and return SecurityEventContextProps object.

        Returns:
            SecurityEventContextProps instance
        """
        # TODO: Add validation
        return self._obj
