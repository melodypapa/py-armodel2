"""ReferenceBase AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    ReferrableSubtypesEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
    ARPackage,
)


class ReferenceBase(ARObject):
    """AUTOSAR ReferenceBase."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "global_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # globalElements
        "global_ins": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ARPackage,
        ),  # globalIns
        "is_default": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # isDefault
        "package": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ARPackage,
        ),  # package
        "short_label": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # shortLabel
    }

    def __init__(self) -> None:
        """Initialize ReferenceBase."""
        super().__init__()
        self.global_elements: list[ReferrableSubtypesEnum] = []
        self.global_ins: list[ARPackage] = []
        self.is_default: Boolean = None
        self.package: Optional[ARPackage] = None
        self.short_label: Identifier = None


class ReferenceBaseBuilder:
    """Builder for ReferenceBase."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceBase = ReferenceBase()

    def build(self) -> ReferenceBase:
        """Build and return ReferenceBase object.

        Returns:
            ReferenceBase instance
        """
        # TODO: Add validation
        return self._obj
