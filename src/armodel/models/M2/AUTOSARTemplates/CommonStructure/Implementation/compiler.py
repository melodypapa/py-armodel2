"""Compiler AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Compiler(Identifiable):
    """AUTOSAR Compiler."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "name": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # name
        "options": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # options
        "vendor": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vendor
        "version": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # version
    }

    def __init__(self) -> None:
        """Initialize Compiler."""
        super().__init__()
        self.name: Optional[String] = None
        self.options: Optional[String] = None
        self.vendor: Optional[String] = None
        self.version: Optional[String] = None


class CompilerBuilder:
    """Builder for Compiler."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Compiler = Compiler()

    def build(self) -> Compiler:
        """Build and return Compiler object.

        Returns:
            Compiler instance
        """
        # TODO: Add validation
        return self._obj
