"""DiagnosticAuthRoleProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
    DiagnosticAuthRole,
)


class DiagnosticAuthRoleProxy(ARObject):
    """AUTOSAR DiagnosticAuthRoleProxy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthRoleProxy."""
        super().__init__()
        self.authentication_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAuthRoleProxy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize authentication_refs (list to container "AUTHENTICATION-REFS")
        if self.authentication_refs:
            wrapper = ET.Element("AUTHENTICATION-REFS")
            for item in self.authentication_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticAuthRole")
                if serialized is not None:
                    child_elem = ET.Element("AUTHENTICATION-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthRoleProxy":
        """Deserialize XML element to DiagnosticAuthRoleProxy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthRoleProxy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse authentication_refs (list from container "AUTHENTICATION-REFS")
        obj.authentication_refs = []
        container = SerializationHelper.find_child_element(element, "AUTHENTICATION-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.authentication_refs.append(child_value)

        return obj



class DiagnosticAuthRoleProxyBuilder:
    """Builder for DiagnosticAuthRoleProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthRoleProxy = DiagnosticAuthRoleProxy()

    def build(self) -> DiagnosticAuthRoleProxy:
        """Build and return DiagnosticAuthRoleProxy object.

        Returns:
            DiagnosticAuthRoleProxy instance
        """
        # TODO: Add validation
        return self._obj
