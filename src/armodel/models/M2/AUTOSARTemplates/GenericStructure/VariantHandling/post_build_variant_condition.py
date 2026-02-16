"""PostBuildVariantCondition AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class PostBuildVariantCondition(ARObject):
    """AUTOSAR PostBuildVariantCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "matching": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=any (PostBuildVariant),
        ),  # matching
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize PostBuildVariantCondition."""
        super().__init__()
        self.matching: Any = None
        self.value: Integer = None


class PostBuildVariantConditionBuilder:
    """Builder for PostBuildVariantCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCondition = PostBuildVariantCondition()

    def build(self) -> PostBuildVariantCondition:
        """Build and return PostBuildVariantCondition object.

        Returns:
            PostBuildVariantCondition instance
        """
        # TODO: Add validation
        return self._obj
