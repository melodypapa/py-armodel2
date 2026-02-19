"""ApplicationError AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 108)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1996)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class ApplicationError(Identifiable):
    """AUTOSAR ApplicationError."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    error_code: Optional[Integer]
    def __init__(self) -> None:
        """Initialize ApplicationError."""
        super().__init__()
        self.error_code: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationError":
        """Deserialize XML element to ApplicationError object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationError object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationError, cls).deserialize(element)

        # Parse error_code
        child = ARObject._find_child_element(element, "ERROR-CODE")
        if child is not None:
            error_code_value = child.text
            obj.error_code = error_code_value

        return obj



class ApplicationErrorBuilder:
    """Builder for ApplicationError."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationError = ApplicationError()

    def build(self) -> ApplicationError:
        """Build and return ApplicationError object.

        Returns:
            ApplicationError instance
        """
        # TODO: Add validation
        return self._obj
