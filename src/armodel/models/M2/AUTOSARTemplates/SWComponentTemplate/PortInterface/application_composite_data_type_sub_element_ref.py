"""ApplicationCompositeDataTypeSubElementRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ApplicationCompositeDataTypeSubElementRef(SubElementRef):
    """AUTOSAR ApplicationCompositeDataTypeSubElementRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application: Optional[Any]
    def __init__(self) -> None:
        """Initialize ApplicationCompositeDataTypeSubElementRef."""
        super().__init__()
        self.application: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationCompositeDataTypeSubElementRef":
        """Deserialize XML element to ApplicationCompositeDataTypeSubElementRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationCompositeDataTypeSubElementRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationCompositeDataTypeSubElementRef, cls).deserialize(element)

        # Parse application
        child = ARObject._find_child_element(element, "APPLICATION")
        if child is not None:
            application_value = child.text
            obj.application = application_value

        return obj



class ApplicationCompositeDataTypeSubElementRefBuilder:
    """Builder for ApplicationCompositeDataTypeSubElementRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeDataTypeSubElementRef = ApplicationCompositeDataTypeSubElementRef()

    def build(self) -> ApplicationCompositeDataTypeSubElementRef:
        """Build and return ApplicationCompositeDataTypeSubElementRef object.

        Returns:
            ApplicationCompositeDataTypeSubElementRef instance
        """
        # TODO: Add validation
        return self._obj
