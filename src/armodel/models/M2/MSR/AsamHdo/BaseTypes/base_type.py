"""BaseType AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_definition import (
    BaseTypeDefinition,
)


class BaseType(ARElement):
    """AUTOSAR BaseType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=BaseTypeDefinition,
        ),  # baseType
    }

    def __init__(self) -> None:
        """Initialize BaseType."""
        super().__init__()
        self.base_type: BaseTypeDefinition = None


class BaseTypeBuilder:
    """Builder for BaseType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BaseType = BaseType()

    def build(self) -> BaseType:
        """Build and return BaseType object.

        Returns:
            BaseType instance
        """
        # TODO: Add validation
        return self._obj
