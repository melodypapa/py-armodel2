"""DiagnosticAuthRoleProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    authentications: list[DiagnosticAuthRole]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthRoleProxy."""
        super().__init__()
        self.authentications: list[DiagnosticAuthRole] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAuthRoleProxy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize authentications (list to container "AUTHENTICATIONS")
        if self.authentications:
            wrapper = ET.Element("AUTHENTICATIONS")
            for item in self.authentications:
                serialized = ARObject._serialize_item(item, "DiagnosticAuthRole")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Parse authentications (list from container "AUTHENTICATIONS")
        obj.authentications = []
        container = ARObject._find_child_element(element, "AUTHENTICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.authentications.append(child_value)

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
