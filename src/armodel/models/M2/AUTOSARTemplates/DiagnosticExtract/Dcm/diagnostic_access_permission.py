"""DiagnosticAccessPermission AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
    DiagnosticAuthRole,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_security_level import (
    DiagnosticSecurityLevel,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_session import (
    DiagnosticSession,
)


class DiagnosticAccessPermission(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAccessPermission."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication: Optional[DiagnosticAuthRole]
    diagnostic_sessions: list[DiagnosticSession]
    environmental: Optional[Any]
    security_levels: list[DiagnosticSecurityLevel]
    def __init__(self) -> None:
        """Initialize DiagnosticAccessPermission."""
        super().__init__()
        self.authentication: Optional[DiagnosticAuthRole] = None
        self.diagnostic_sessions: list[DiagnosticSession] = []
        self.environmental: Optional[Any] = None
        self.security_levels: list[DiagnosticSecurityLevel] = []
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAccessPermission to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAccessPermission, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentication
        if self.authentication is not None:
            serialized = ARObject._serialize_item(self.authentication, "DiagnosticAuthRole")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTHENTICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_sessions (list to container "DIAGNOSTIC-SESSIONS")
        if self.diagnostic_sessions:
            wrapper = ET.Element("DIAGNOSTIC-SESSIONS")
            for item in self.diagnostic_sessions:
                serialized = ARObject._serialize_item(item, "DiagnosticSession")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize environmental
        if self.environmental is not None:
            serialized = ARObject._serialize_item(self.environmental, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENVIRONMENTAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_levels (list to container "SECURITY-LEVELS")
        if self.security_levels:
            wrapper = ET.Element("SECURITY-LEVELS")
            for item in self.security_levels:
                serialized = ARObject._serialize_item(item, "DiagnosticSecurityLevel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAccessPermission":
        """Deserialize XML element to DiagnosticAccessPermission object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAccessPermission object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAccessPermission, cls).deserialize(element)

        # Parse authentication
        child = ARObject._find_child_element(element, "AUTHENTICATION")
        if child is not None:
            authentication_value = ARObject._deserialize_by_tag(child, "DiagnosticAuthRole")
            obj.authentication = authentication_value

        # Parse diagnostic_sessions (list from container "DIAGNOSTIC-SESSIONS")
        obj.diagnostic_sessions = []
        container = ARObject._find_child_element(element, "DIAGNOSTIC-SESSIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.diagnostic_sessions.append(child_value)

        # Parse environmental
        child = ARObject._find_child_element(element, "ENVIRONMENTAL")
        if child is not None:
            environmental_value = child.text
            obj.environmental = environmental_value

        # Parse security_levels (list from container "SECURITY-LEVELS")
        obj.security_levels = []
        container = ARObject._find_child_element(element, "SECURITY-LEVELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.security_levels.append(child_value)

        return obj



class DiagnosticAccessPermissionBuilder:
    """Builder for DiagnosticAccessPermission."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAccessPermission = DiagnosticAccessPermission()

    def build(self) -> DiagnosticAccessPermission:
        """Build and return DiagnosticAccessPermission object.

        Returns:
            DiagnosticAccessPermission instance
        """
        # TODO: Add validation
        return self._obj
