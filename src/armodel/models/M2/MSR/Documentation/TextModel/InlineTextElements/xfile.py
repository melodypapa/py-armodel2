"""Xfile AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Xfile(SingleLanguageReferrable):
    """AUTOSAR Xfile."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tool": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tool
        "tool_version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # toolVersion
        "url": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (Url),
        ),  # url
    }

    def __init__(self) -> None:
        """Initialize Xfile."""
        super().__init__()
        self.tool: Optional[String] = None
        self.tool_version: Optional[String] = None
        self.url: Optional[Any] = None


class XfileBuilder:
    """Builder for Xfile."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xfile = Xfile()

    def build(self) -> Xfile:
        """Build and return Xfile object.

        Returns:
            Xfile instance
        """
        # TODO: Add validation
        return self._obj
