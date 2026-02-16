"""ApplicationArrayDataType AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import (
    ApplicationCompositeDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class ApplicationArrayDataType(ApplicationCompositeDataType):
    """AUTOSAR ApplicationArrayDataType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dynamic_array": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dynamicArray
        "element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ApplicationArray),
        ),  # element
    }

    def __init__(self) -> None:
        """Initialize ApplicationArrayDataType."""
        super().__init__()
        self.dynamic_array: Optional[String] = None
        self.element: Optional[Any] = None


class ApplicationArrayDataTypeBuilder:
    """Builder for ApplicationArrayDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationArrayDataType = ApplicationArrayDataType()

    def build(self) -> ApplicationArrayDataType:
        """Build and return ApplicationArrayDataType object.

        Returns:
            ApplicationArrayDataType instance
        """
        # TODO: Add validation
        return self._obj
