"""AbstractValueRestriction AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    PositiveInteger,
    RegularExpression,
)


class AbstractValueRestriction(ARObject):
    """AUTOSAR AbstractValueRestriction."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # max
        "max_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxLength
        "min": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # min
        "min_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minLength
        "pattern": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # pattern
    }

    def __init__(self) -> None:
        """Initialize AbstractValueRestriction."""
        super().__init__()
        self.max: Optional[Limit] = None
        self.max_length: Optional[PositiveInteger] = None
        self.min: Optional[Limit] = None
        self.min_length: Optional[PositiveInteger] = None
        self.pattern: Optional[RegularExpression] = None


class AbstractValueRestrictionBuilder:
    """Builder for AbstractValueRestriction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractValueRestriction = AbstractValueRestriction()

    def build(self) -> AbstractValueRestriction:
        """Build and return AbstractValueRestriction object.

        Returns:
            AbstractValueRestriction instance
        """
        # TODO: Add validation
        return self._obj
