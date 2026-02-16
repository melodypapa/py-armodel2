"""AtpInstanceRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_classifier import (
    AtpClassifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_prototype import (
    AtpPrototype,
)


class AtpInstanceRef(ARObject):
    """AUTOSAR AtpInstanceRef."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "atp_base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=AtpClassifier,
        ),  # atpBase
        "atp_contexts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AtpPrototype,
        ),  # atpContexts
        "atp_target": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=AtpFeature,
        ),  # atpTarget
    }

    def __init__(self) -> None:
        """Initialize AtpInstanceRef."""
        super().__init__()
        self.atp_base: AtpClassifier = None
        self.atp_contexts: list[AtpPrototype] = []
        self.atp_target: AtpFeature = None


class AtpInstanceRefBuilder:
    """Builder for AtpInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpInstanceRef = AtpInstanceRef()

    def build(self) -> AtpInstanceRef:
        """Build and return AtpInstanceRef object.

        Returns:
            AtpInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
