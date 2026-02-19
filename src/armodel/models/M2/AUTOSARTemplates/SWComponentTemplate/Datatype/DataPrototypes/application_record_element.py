"""ApplicationRecordElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 261)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1997)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 43)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import (
    ApplicationCompositeElementDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):
    """AUTOSAR ApplicationRecordElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    is_optional: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ApplicationRecordElement."""
        super().__init__()
        self.is_optional: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationRecordElement":
        """Deserialize XML element to ApplicationRecordElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationRecordElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationRecordElement, cls).deserialize(element)

        # Parse is_optional
        child = ARObject._find_child_element(element, "IS-OPTIONAL")
        if child is not None:
            is_optional_value = child.text
            obj.is_optional = is_optional_value

        return obj



class ApplicationRecordElementBuilder:
    """Builder for ApplicationRecordElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationRecordElement = ApplicationRecordElement()

    def build(self) -> ApplicationRecordElement:
        """Build and return ApplicationRecordElement object.

        Returns:
            ApplicationRecordElement instance
        """
        # TODO: Add validation
        return self._obj
