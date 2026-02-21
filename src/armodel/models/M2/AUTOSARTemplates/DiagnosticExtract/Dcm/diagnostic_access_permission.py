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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    diagnostic_session_refs: list[ARRef]
    environmental_ref: Optional[Any]
    security_level_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticAccessPermission."""
        super().__init__()
        self.authentication: Optional[DiagnosticAuthRole] = None
        self.diagnostic_session_refs: list[ARRef] = []
        self.environmental_ref: Optional[Any] = None
        self.security_level_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAccessPermission to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAccessPermission, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

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

        # Serialize diagnostic_session_refs (list to container "DIAGNOSTIC-SESSION-REFS")
        if self.diagnostic_session_refs:
            wrapper = ET.Element("DIAGNOSTIC-SESSION-REFS")
            for item in self.diagnostic_session_refs:
                serialized = ARObject._serialize_item(item, "DiagnosticSession")
                if serialized is not None:
                    child_elem = ET.Element("DIAGNOSTIC-SESSION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize environmental_ref
        if self.environmental_ref is not None:
            serialized = ARObject._serialize_item(self.environmental_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENVIRONMENTAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_level_refs (list to container "SECURITY-LEVEL-REFS")
        if self.security_level_refs:
            wrapper = ET.Element("SECURITY-LEVEL-REFS")
            for item in self.security_level_refs:
                serialized = ARObject._serialize_item(item, "DiagnosticSecurityLevel")
                if serialized is not None:
                    child_elem = ET.Element("SECURITY-LEVEL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
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

        # Parse diagnostic_session_refs (list from container "DIAGNOSTIC-SESSION-REFS")
        obj.diagnostic_session_refs = []
        container = ARObject._find_child_element(element, "DIAGNOSTIC-SESSION-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.diagnostic_session_refs.append(child_value)

        # Parse environmental_ref
        child = ARObject._find_child_element(element, "ENVIRONMENTAL-REF")
        if child is not None:
            environmental_ref_value = ARRef.deserialize(child)
            obj.environmental_ref = environmental_ref_value

        # Parse security_level_refs (list from container "SECURITY-LEVEL-REFS")
        obj.security_level_refs = []
        container = ARObject._find_child_element(element, "SECURITY-LEVEL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.security_level_refs.append(child_value)

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
